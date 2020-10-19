import asyncio

from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient


async def main():
    client = AsyncIOMotorClient("localhost", 27017)
    db = client["learn__pypi__motor"]
    col: AgnosticCollection = db["test"]

    await col.delete_many({})

    await col.insert_many([{"name": "n1", "value": 10}, {"name": "n2", "value": 20}])

    res = await col.find_one({"name": "n1"})
    print("find_one", res)

    cur = col.find({})
    for doc in await cur.to_list(None):
        print("doc", doc)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
