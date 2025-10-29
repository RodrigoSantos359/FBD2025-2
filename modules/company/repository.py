from modules.company.schemas import CompanyCreate
from core.db import DataBase

class CompanyRepository:
    QUERY_LISTAR = "SELECT id, nome, cnpj, status FROM empresa" # Tabela é 'empresa' no DB, não 'company'
    QUERY_BUSCAR_ID = "SELECT id, nome, cnpj, status FROM empresa WHERE id = %s"
    QUERY_CRIAR = "INSERT INTO empresa (nome, cnpj, status) VALUES (%s, %s, %s) RETURNING id, nome, cnpj, status"
    QUERY_ATUALIZAR = "UPDATE empresa SET nome = %s, cnpj = %s, status = %s WHERE id = %s RETURNING id, nome, cnpj, status"
    QUERY_DELETAR = "DELETE FROM empresa WHERE id = %s"
    
    def _row_to_company(self, row):
        """Converte o resultado da tupla do banco de dados em um dicionário."""
        if not row:
            return None
        return {
            "id": row[0],
            "nome": row[1],
            "cnpj": row[2],
            "status": row[3]
        }

    def listar(self):
        db = DataBase()
        rows = db.execute(self.QUERY_LISTAR)
        return [self._row_to_company(row) for row in rows]

    def buscar_por_id(self, company_id: int):
        db = DataBase()
        row = db.execute(self.QUERY_BUSCAR_ID % company_id, many=False)
        return self._row_to_company(row)

    def criar(self, company: CompanyCreate):
        db = DataBase()
        
        query = self.QUERY_CRIAR % (
            f"'{company.nome}'", 
            f"'{company.cnpj}'", 
            f"'{company.status}'" # Literal é tratado como string
        )
        row = db.commit(query)
        
        return self._row_to_company(row)

    def atualizar(self, company_id: int, company_data: CompanyCreate):
        db = DataBase()
        
        query = self.QUERY_ATUALIZAR % (
            f"'{company_data.nome}'", 
            f"'{company_data.cnpj}'", 
            f"'{company_data.status}'",
            company_id
        )
        row = db.commit(query)
        
        return self._row_to_company(row)

    def deletar(self, company_id: int):
        db = DataBase()
        db.commit(self.QUERY_DELETAR % company_id)
        return {"mensagem": "Empresa deletada com sucesso"}


