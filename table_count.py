import asyncpg
import asyncio
import time

async def get_count(table_name, connection):
    query = f"SELECT COUNT(*) FROM {table_name}"
    count = await connection.fetchval(query)
    print(f"Count of rows in {table_name}: {count}")

async def main():
    # Create connections to the database
    connections = await asyncio.gather(
        asyncpg.connect(user='postgres', password='password', database='postgres', host='localhost'),
        asyncpg.connect(user='postgres', password='password', database='postgres', host='localhost'),
        asyncpg.connect(user='postgres', password='password', database='postgres', host='localhost')
    )

    # Define the tables for which you want to fetch counts
    tables = ['daily_sales', 'employees', 'students']

    start_time = time.time()

    # Create tasks to fetch counts for each table using each connection
    tasks = [get_count(table, connection) for table, connection in zip(tables, connections)]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time} seconds")

    # Close the database connections
    for connection in connections:
        await connection.close()

# Run the main function
asyncio.run(main())
