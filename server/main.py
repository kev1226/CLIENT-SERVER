from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List
from fastapi.middleware.cors import CORSMiddleware

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        movies_data = [
            Movie(title="The Silence of the Lambs", director="Jonathan Demme"),
            Movie(title="Lady Snowblood", director="Toshiya Fujita"),
            Movie(title="Pulp Fiction", director="Quentin Tarantino"),
            Movie(title="Scarface", director="Brian De Palma"),
            Movie(title="Fight Club", director="David Fincher"),
        ]
        return movies_data

schema = strawberry.Schema(query=Query)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.get("/")
def index():
    return {"message": "Welcome to the GraphQL API"}

app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
