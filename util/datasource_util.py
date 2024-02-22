import psycopg2


def get_datasource(database: str, db_info: dict) -> psycopg2.extensions.connection:
	print('建立数据库链接')
	db_info['database'] = database
	return psycopg2.connect(**db_info)


def query_one(cursor: psycopg2.extensions.cursor, sql):
	cursor.execute(sql)
	return cursor.fetchone()
