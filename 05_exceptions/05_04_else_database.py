# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.


import sqlalchemy
#from projects import keys 

try:
    engine = sqlalchemy.create_engine('mysql+pymysql://'+ 'wrong' + ':' + 'wrong' + '@localhost/recipes')
    connection = engine.connect()

    metadata = sqlalchemy.MetaData()  
    recipe_table = sqlalchemy.Table('recipe', metadata, autoload_with=engine)

except:
    print("Connection Error")
else:
    stmt = sqlalchemy.select(recipe_table.columns.recipetitle)
    results = connection.execute(stmt)
    output = results.fetchall()

    print(output)