from core.db import DataBase
from modules.company.schemas import CompanyCreate


class CompanyRepository:
    QUERY_COMPANIES = "SELECT id, name FROM company"
    QUERY_COMPANY_ID = "SELECT id, name FROM company where id = %s"
    QUERY_CREATE_COMPANY = 'INSERT INTO company (name) VALUES (%s) RETURNING id;'

    def get_all(self):
        db = DataBase()
        companies = db.execute(self.QUERY_COMPANIES)
        results = []
        for company in companies:
            results.append({"id": company[0], "name": company[1]})
        return results

    def save(self, company: CompanyCreate):
        db = DataBase()
        query = self.QUERY_CREATE_COMPANY % f"'{company.name}'"
        result = db.commit(query)
        return {"id": result[0], "name": company.name}

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_COMPANY_ID % id
        company = db.execute(query, many=False)
        if company:
            return {"id": company[0], "name": company[1]}
        return {}