class Hero(SQLModel, table=True):  # DAO creates hero
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

hero1
{
    "name": "Peter Parker",
    "secret_name": "Spiderman"
}

hero02
{
    "name": "Bruce Banner",
    "secret_name": "Hulk"
}

hero03
{
    "name": "Tony Stark",
    "secret_name": "Ironman"
}