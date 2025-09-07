# backend/app.py

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional

from cve_checker import run_cve_scan

# Define AlertType for GraphQL output
@strawberry.type
class CVEEntry:
    id: str
    description: str
    published: str
    source: str

@strawberry.type
class CVEPackageAlerts:
    package: str
    entries: List[CVEEntry]

@strawberry.type
class Query:
    ping: str = "GraphQL is live."

@strawberry.type
class Mutation:

    @strawberry.field
    def scan_cves(self) -> List[CVEPackageAlerts]:
        """Trigger CVE scan and return alerts grouped by package."""
        raw_data = run_cve_scan()
        results = []

        for pkg, entries in raw_data.items():
            cve_entries = [
                CVEEntry(
                    id=e["id"],
                    description=e["description"],
                    published=e["published"],
                    source=e["source"]
                )
                for e in entries
            ]
            results.append(CVEPackageAlerts(package=pkg, entries=cve_entries))

        return results


# Set up Strawberry + FastAPI
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
