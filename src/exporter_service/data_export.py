from src.api.core.container import Container
import src.exporter_service.movielens_export_helper
from src.exporter_service.movielens_export_helper import MovielensHelper
import asyncio

async def export():
    container = Container()
    container.wire(modules=[src.exporter_service.movielens_export_helper])

    await MovielensHelper.export()

if __name__ == "__main__":
    asyncio.run(export())