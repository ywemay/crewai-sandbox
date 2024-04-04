import psycopg2

class DatabaseTools():

  @tool("Create Table in PostgreSQL")
  def create_table(schema, table_name, columns):
    """Useful to create a new table in the given schema with the provided columns."""
    try:
      conn = psycopg2.connect(database="dbname", user="username", password="password", host="localhost")
      cur = conn.cursor()
      cur.execute(f"CREATE TABLE {schema}.{table_name} ({', '.join([col[0] + ' ' + col[1] for col in columns])});")
      conn.commit()
      return f"Table '{table_name}' created successfully in schema '{schema}'."
    except Exception as e:
      return str(e)

  @tool("Run SQL query")
  def run_sql(query):
    """Useful to execute a given SQL query and return the result."""
    try:
      conn = psycopg2.connect(database="dbname", user="username", password="password", host="localhost")
      cur = conn.cursor()
      cur.execute(query)
      result = cur.fetchall()
      return result
    except Exception as e:
      return str(e)