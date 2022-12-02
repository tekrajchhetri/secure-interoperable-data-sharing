# -*- coding: utf-8 -*-
# @Time    : 23.01.22 23:43
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : data_transformation_engine.py
# @Software: PyCharm
import sys
from rdflib import Graph, Literal, XSD, RDF,URIRef
from rdflib import Namespace
import textwrap
from smart_contract.transaction import Transaction
class DataTransformationEngine:
    def generate_shacl_data_graph(self, data):
        """ Transforms the data in JSON format to semantic Knowledge Graphs in JSONLD format,
        i.e., creates the data graph
        :inputs: JSON format
            Example Input:
                {'observedproperty': 'STI_W201_temperature', 'observationsensorid': 'DHT11', 'observationresult': 22.0,
                'resultobservationtime': '2022-11-24T09:54:19:782843', 'observationid': 'DHT11_202211245419782843',
                'hashvalue': '064389e8141c76cdffbc9f3424b65a9562c7efaf96c3f97f0a929928feb3328c',
                'blockchainhashvalue': '0x510068715be38aa9e7ad5e600748644f858ae908f1be51adc5e24c81aa862bcc'}
        :return: Trnasformed Knowledge Graph in JSONLD representation
            Example Output:
                {
                  "@context": {
                    "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
                    "sosa": "http://www.w3.org/ns/sosa/",
                    "sricats": "http://www.tekrajchhetri.com/sricats/",
                    "xsd": "http://www.w3.org/2001/XMLSchema#"
                  },
                  "@graph": [
                    {
                      "@id": "http://www.w3.org/ns/sosa/Sensor/DHT11",
                      "@type": "sosa:Sensor",
                      "sosa:observes": {
                        "@id": "http://www.w3.org/ns/sosa/Observation/DHT11_202211242518407674"
                      }
                    },
                    {
                      "@id": "http://www.w3.org/ns/sosa/Observation/DHT11_202211242518407674",
                      "@type": "sosa:Observation",
                      "om:hasUnit": {
                        "@id": "om:percent"
                      },
                      "sosa:hasSimpleResult": 33.0,
                      "sosa:madeBySensor": {
                        "@id": "http://www.w3.org/ns/sosa/Sensor/DHT11"
                      },
                      "sosa:observedProperty": {
                        "@id": "http://www.w3.org/ns/sosa/observedProperty/STI_W201_humidity"
                      },
                      "sosa:resultTime": {
                        "@type": "xsd:dateTime",
                        "@value": "2022-11-24T09:25:18"
                      },
                      "sricats:hasBlockChainHash": "0x00e23a616470fc2004c33a0fd8fd444c3914d5244cfb0cbdd7a73723b3320188",
                    }
                  ]
                }
        """
        SRICATS = Namespace("http://www.tekrajchhetri.com/sricats/")
        SOSA = Namespace("http://www.w3.org/ns/sosa/")
        OM = Namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
        g = Graph()
        g.bind('sosa', SOSA)
        g.bind('sricats', SRICATS)
        g.bind('om', OM)
        sensor = URIRef(f"{SOSA['Sensor']}/{data['observationsensorid']}")
        obs = URIRef(f"{SOSA['Observation']}/{data['observationid']}")
        g.add((sensor, RDF.type, SOSA['Sensor']))
        g.add((sensor, SOSA["observes"], obs))
        g.add((obs, RDF.type, SOSA['Observation']))
        g.add((obs, SOSA['madeBySensor'], sensor))
        g.add((obs, SOSA['observedProperty'], URIRef(f"{SOSA['observedProperty']}/{data['observedproperty']}")))
        g.add((obs, SOSA['hasSimpleResult'], Literal(data['observationresult'], datatype=XSD.double)))
        g.add((obs, SOSA['resultTime'], Literal(data['resultobservationtime'], datatype=XSD.dateTime)))
        if "temperature" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["degreeCelsius"]))
        elif "humidity" in data['observedproperty']:
            g.add((obs, OM['hasUnit'], OM["percent"]))
        g.add((obs, SRICATS['hasBlockChainHash'], Literal(data['blockchainhashvalue'], datatype=XSD.string)))
        g.add((obs, SRICATS['hasTrustabilityScore'], Literal(data['trustabilityscore'], datatype=XSD.float)))
        context = {"sricats": "http://www.tekrajchhetri.com/sricats/",
                   "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
                   "sosa": "http://www.w3.org/ns/sosa/",
                   "xsd": "http://www.w3.org/2001/XMLSchema#"
                   }
        return g.serialize(format="json-ld", context=context)

    def parse_kg_data_to_turtle(self, rdf_data):
        """:Convert JSONLD to Turtle
            :inputs: JSONLD
               Example Input:
                    {
                      "@context": {
                        "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
                        "sosa": "http://www.w3.org/ns/sosa/",
                        "sricats": "http://www.tekrajchhetri.com/sricats/",
                        "xsd": "http://www.w3.org/2001/XMLSchema#"
                      },
                      "@graph": [
                        {
                          "@id": "http://www.w3.org/ns/sosa/Sensor/DHT11",
                          "@type": "sosa:Sensor",
                          "sosa:observes": {
                            "@id": "http://www.w3.org/ns/sosa/Observation/DHT11_202211242518407674"
                          }
                        },
                        {
                          "@id": "http://www.w3.org/ns/sosa/Observation/DHT11_202211242518407674",
                          "@type": "sosa:Observation",
                          "om:hasUnit": {
                            "@id": "om:percent"
                          },
                          "sosa:hasSimpleResult": 33.0,
                          "sosa:madeBySensor": {
                            "@id": "http://www.w3.org/ns/sosa/Sensor/DHT11"
                          },
                          "sosa:observedProperty": {
                            "@id": "http://www.w3.org/ns/sosa/observedProperty/STI_W201_humidity"
                          },
                          "sosa:resultTime": {
                            "@type": "xsd:dateTime",
                            "@value": "2022-11-24T09:25:18"
                          },
                          "sricats:hasBlockChainHash": "0x00e23a616470fc2004c33a0fd8fd444c3914d5244cfb0cbdd7a73723b3320188",
                          "sricats:hasHash": "7a2615a501c47bb0d0a27cafeebce02141f54232c141cb009ee70e5150226596"
                        }
                      ]
                    }
            :return: Knowledge graph representation in Turtle format.
                Example Output:
                    @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
                    @prefix sosa: <http://www.w3.org/ns/sosa/> .
                    @prefix sricats: <http://www.tekrajchhetri.com/sricats/> .
                    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

                    <http://www.w3.org/ns/sosa/Observation/DHT11_202211240149872310> a sosa:Observation ;
                        om:hasUnit om:percent ;
                        sricats:hasBlockChainHash "0x359703b4d004537f35a602a76f3d59a77914481e0ee9bdbcdf02f716bc924ba4" ;
                        sricats:hasHash "65bd3244dea6e8db19e19827859a8bc14d6668a01337dcdba9a108ef7541e2ff" ;
                        sosa:hasSimpleResult 3.2e+01 ;
                        sosa:madeBySensor <http://www.w3.org/ns/sosa/Sensor/DHT11> ;
                        sosa:observedProperty <http://www.w3.org/ns/sosa/observedProperty/STI_W201_humidity> ;
                        sosa:resultTime "2022-11-24T10:01:49"^^xsd:dateTime .

                    <http://www.w3.org/ns/sosa/Sensor/DHT11> a sosa:Sensor ;
                        sosa:observes <http://www.w3.org/ns/sosa/Observation/DHT11_202211240149872310> .

        """
        return Graph().parse(data=rdf_data, format='json-ld').serialize(format="turtle")

    def transform(self, rdf_data):
        """ Converts Turtle  representation of knowledge graphs into subject, predicate and object format for migration.
        :param rdf_data: Turtle representation of knowledge graphs. Should be of type RDFlib Graph
            Example:
                    @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
                    @prefix sosa: <http://www.w3.org/ns/sosa/> .
                    @prefix sricats: <http://www.tekrajchhetri.com/sricats/> .
                    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

                    <http://www.w3.org/ns/sosa/Observation/DHT11_202211240149872310> a sosa:Observation ;
                        om:hasUnit om:percent ;
                        sricats:hasBlockChainHash "0x359703b4d004537f35a602a76f3d59a77914481e0ee9bdbcdf02f716bc924ba4" ;
                        sricats:hasHash "65bd3244dea6e8db19e19827859a8bc14d6668a01337dcdba9a108ef7541e2ff" ;
                        sosa:hasSimpleResult 3.2e+01 ;
                        sosa:madeBySensor <http://www.w3.org/ns/sosa/Sensor/DHT11> ;
                        sosa:observedProperty <http://www.w3.org/ns/sosa/observedProperty/STI_W201_humidity> ;
                        sosa:resultTime "2022-11-24T10:01:49"^^xsd:dateTime .

                    <http://www.w3.org/ns/sosa/Sensor/DHT11> a sosa:Sensor ;
                        sosa:observes <http://www.w3.org/ns/sosa/Observation/DHT11_202211240149872310> .
        :return:
            Example:
                <http://www.w3.org/ns/sosa/Observation/DHT11_202211240150991256> <http://www.w3.org/ns/sosa/hasSimpleResult> "22.0"^^<http://www.w3.org/2001/XMLSchema#double> .
                <http://www.w3.org/ns/sosa/Observation/DHT11_202211240150991256> <http://www.w3.org/ns/sosa/observedProperty> <http://www.w3.org/ns/sosa/observedProperty/STI_W201_temperature> .
                <http://www.w3.org/ns/sosa/Observation/DHT11_202211240150991256> <http://www.tekrajchhetri.com/sricats/hasBlockChainHash> "0xacea65895c77b926e0e3cb931e7217246e61001dea85fdedf42a48ba3851177f" .
                <http://www.w3.org/ns/sosa/Observation/DHT11_202211240150991256> <http://www.w3.org/ns/sosa/madeBySensor> <http://www.w3.org/ns/sosa/Sensor/DHT11> .
                <http://www.w3.org/ns/sosa/Observation/DHT11_202211240150991256> <http://www.tekrajchhetri.com/sricats/hasHash> "e2d5c4e7532e836d28eb38ab31e04b33e74733ef2abcf0ace2b8acd846a43dc3" .

        """
        transformed_data = ""
        for subject, predicate, obj in rdf_data:
            transformed_data = transformed_data + subject.n3() + " " + predicate.n3() + " " + obj.n3() + " . \n"
            print("##########################################################################################")
            print(f"######################  DATA for Migration                          #####################")
            print("##########################################################################################")
        return transformed_data


