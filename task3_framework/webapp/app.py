from bumbo.api import API

from auth import login_required, TokenMiddleware, STATIC_TOKEN, on_exception
from storage import SampleStorage


app = API()
sample_storage = SampleStorage()
sample_storage.create(seniority=9, home=1, time=60, age=30, marital=2, records=1, job=3, expenses=73, income=129, assets=0, debt=0, amount=800, price=846, predict=True)
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
