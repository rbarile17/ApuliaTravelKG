import pandas as pd

results = pd.read_csv("results.csv", na_filter=False)

NAMESPACES = [
    "https://w3id.org/italia/onto/CLV/",
    "https://w3id.org/italia/onto/SM/",
    "https://w3id.org/italia/onto/AccessCondition/",
    "https://w3id.org/italia/onto/TI/",
    "https://w3id.org/italia/onto/POI/",
    "https://w3id.org/italia/onto/l0/",
    "https://example.org/td/",
    "https://w3id.org/italia/onto/CLV/Geometry/",
    "https://w3id.org/italia/onto/SM/Rating/",
    "https://w3id.org/italia/onto/SM/Review/",
    "https://w3id.org/italia/onto/SM/WebSite/",
    "https://w3id.org/italia/onto/SM/Telephone/",
    "https://w3id.org/italia/onto/SM/Email/",
    "https://w3id.org/italia/onto/SM/ContactPoint/",
    "https://w3id.org/italia/onto/CLV/AddressArea/",
    "https://w3id.org/italia/onto/CLV/StreetToponym/",
    "https://w3id.org/italia/onto/CLV/StreetNumber/",
    "https://w3id.org/italia/onto/CLV/City/",
    "https://w3id.org/italia/onto/CLV/Province/",
    "https://w3id.org/italia/onto/CLV/Address/",
    "https://w3id.org/italia/onto/CLV/OpeningHours/",
    "https://w3id.org/italia/onto/POI/PointOfInterest/",
]

def get_local_name(iri: str) -> str:
    for ns in sorted(NAMESPACES, key=len, reverse=True):
        if iri.startswith(ns):
            if iri == ns.rstrip("/"):
                return iri.split("/")[-1]
            return iri[len(ns):]
    return iri

results = results.groupby("entity", as_index=False)["class"].agg(set)
results = results.rename(columns={"class": "classes"})
results["entity"] = results["entity"].map(get_local_name)

results.to_csv("entity_classes.csv", index=False)
