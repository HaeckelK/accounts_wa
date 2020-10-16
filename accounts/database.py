from accounts.databasetools import Database, Results


class AccountsDatabase(Database):
    schema = '''CREATE TABLE IF NOT EXISTS upload
                (id INTEGER PRIMARY KEY,
                original_name TEXT,
                name TEXT,
                document_type TEXT,
                upload_function TEXT,
                form_data TEXT,
                date_added INT,
                time_added INT,
                is_deleted INT,
                is_archived INT,
                is_processed INT);'''

    def insert_upload(self, original_name: str, name: str, document_type: str, upload_function: str, form_data: str,
                      date_added: int, time_added: int, is_deleted: int, is_archived: int, is_processed: int):
        params = (original_name, name, document_type, upload_function, form_data, date_added, time_added, is_deleted,
                  is_archived, is_processed)
        new_id = self.insert('''INSERT INTO upload(original_name, name, document_type, upload_function, form_data, date_added, time_added, is_deleted, is_archived, is_processed) VALUES(?,?,?,?,?,?,?,?,?,?)''', params)
        return new_id

    def get_all(self, table: str):
        cursor = self.query(f'''select *
                               from {table}''')
        return Results(cursor).fetchall_dict_factory()

    def get_all_upload(self):
        return self.get_all('upload')    
