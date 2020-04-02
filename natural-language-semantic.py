import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, RelationsOptions, EmotionOptions, EntitiesOptions, SemanticRolesOptions, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
service = NaturalLanguageUnderstandingV1(
    version='2020-03-31',
    authenticator=authenticator)
service.set_service_url('{url}}')


def nlp1():

    response = service.analyze(
    text='Who is the president of Brazil?',
    features=Features(
        concepts=ConceptsOptions(),
        emotion=EmotionOptions(),
        entities=EntitiesOptions(),
        sentiment=SentimentOptions(),
        ))

    print(json.dumps(response.result, indent=2))


def nlp2():

    response = service.analyze(
    text='Steve Jobs is the founder of Apple',
    features=Features(
        entities=EntitiesOptions(),
        semantic_roles=SemanticRolesOptions(),
    ))

    print(json.dumps(response.result, indent=2))


if __name__ == "__main__":
    
    nlp2()

