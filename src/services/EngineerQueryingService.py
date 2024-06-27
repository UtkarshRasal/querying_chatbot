from config.defaults import Constants
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from src.Utils.sql_connection import get_connection


class QueryModes:
    PRECISE = '0'
    BALANCED = '1'
    BASIC = '2'

pinecone = Pinecone(api_key=Constants.PINECONE_SECRET_KEY)

class EngineersQuery:

    def __init__(self):
        try:
            self.model = SentenceTransformer('BAAI/bge-large-en-v1.5')
        except Exception as e:
            print(f"Error loading SentenceTransformer model: {e}")
            self.model = None

        try:
            self.pinecone_index = pinecone.Index(Constants.PINECONE_INDEX)
        except Exception as e:
            print(f"Error initializing Pinecone index: {e}")
            self.pinecone_index = None

        try:
            self.sql_conn = get_connection()
        except Exception as e:
            print(f"Error establishing database connection: {e}")
            self.sql_conn = None

    def get_vector_embeddings(self, text: str):
        if not self.model:
            raise 'Sentence Transformer model is not enabled'
        
        try:
            self.model.encode(text).tolist()
        except:
            print('some error')

    def get_engineers(self, query: str, entities: dict = {}, mode: str = QueryModes.BASIC):
        return self.get_engineers_basic(query)
    
    def get_engineers_basic(self, query: str):
        if not self.pinecone_index:
            raise 'Pincone index is not available'
        
        vector = self.get_vector_embeddings(query)
        if not vector:
            return {}
        
        try:
            query_matches = self.pinecone_index.query(vector=vector, top_k=6, include_metadata=True)
            return query_matches.to_dict()
        except Exception as e:
            print(f"Error querying Pinecone index: {e}")
        
    def get_engineer_details(self, engineers):
        if not self.sql_conn:
            raise ' sql not connected'
        
        try:
            if not engineers.get('matches'):
                return []

            resume_ids = [match['id'] for match in engineers['matches']]
            resume_ids_str = ','.join("'" + str(id) + "'" for id in resume_ids)

            query = """
                SELECT 
                r.resumeId, 
                r.userId, 
                pi.name, 
                pi.email, 
                pi.phone, 
                u.fullTimeStatus, 
                u.workAvailability, 
                u.fullTimeSalaryCurrency, 
                u.fullTimeSalary, 
                u.partTimeSalaryCurrency, 
                u.partTimeSalary, 
                u.fullTimeAvailability, 
                u.partTimeAvailability, 
                u.preferredRole,
                GROUP_CONCAT(DISTINCT we.company) AS WorkExperience,
                GROUP_CONCAT(DISTINCT ed.degree) AS Education,
                GROUP_CONCAT(DISTINCT s.skillName) AS Skills,
                pi.location
                FROM UserResume r
                LEFT JOIN PersonalInformation pi ON r.resumeId = pi.resumeId
                LEFT JOIN MercorUsers u ON r.userId = u.userId
                LEFT JOIN WorkExperience we ON r.resumeId = we.resumeId
                LEFT JOIN Education ed ON r.resumeId = ed.resumeId
                LEFT JOIN MercorUserSkills mus ON r.userId = mus.userId
                LEFT JOIN Skills s ON mus.skillId = s.skillId
                WHERE r.resumeId IN ({})
                GROUP BY r.resumeId, pi.location, pi.name, pi.email, pi.phone;
            """.format(resume_ids_str)

            cursor = self.sql_conn.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()

            column_names = [description[0] for description in cursor.description]
            results = [dict(zip(column_names, row)) for row in records]
            return results

        except Exception as e:
            print(f"Error fetching engineer details from database: {e}")
            return []
    