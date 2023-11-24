from bumbo.api import API

from auth import login_required, TokenMiddleware, STATIC_TOKEN, on_exception
from storage import SampleStorage


app = API()
sample_storage = SampleStorage()

for _ in range(5):
    sample_storage.create(
        seniority=random.randint(0, 30), 
        home=random.choice([x.value for x in HomeType]), 
        time=random.randint(1, 60), 
        age=random.randint(18, 90), 
        marital=random.choice([x.value for x in MaritalType]), 
        records=random.choice([True, False]), 
        job=random.choice([x.value for x in JobType]), 
        expenses=random.randint(0, 9999999), 
        income=random.randint(0, 9999999), 
        assets=random.randint(0, 99999999), 
        debt=random.randint(0, 999999), 
        amount=random.randint(0, 999999), 
        price=random.randint(0, 999999)
    )

app.add_middleware(TokenMiddleware)
app.add_exception_handler(on_exception)


@app.route("/", allowed_methods=["get"])
def index(req, resp):
    samples = sample_storage.all()
    resp.html = app.template("index.html", context={"samples": samples})


@app.route("/login", allowed_methods=["post"])
def login(req, resp):
    resp.json = {"token": STATIC_TOKEN}


@app.route("/samples", allowed_methods=["post"])
@login_required
def create_sample(req, resp):
    sample = sample_storage.create(**req.POST)

    resp.status_code = 201
    resp.json = sample._asdict()


@app.route("/samples/{id:d}", allowed_methods=["delete"])
@login_required
def delete_sample(req, resp, id):
    sample_storage.delete(id)

    resp.status_code = 204
