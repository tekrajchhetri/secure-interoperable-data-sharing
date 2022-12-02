# -*- coding: utf-8 -*-
# @Time    : 10.05.22 16:41
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : shacl_shapes.py
# @Software: PyCharm

class SHACLShapes:
    def temperature(self):
        """ SHACL shape graph for temperature sensor

        Example Data Graph:
            <http://www.w3.org/ns/sosa/Observation/DHT11_202212020001> a sosa:Observation ;
                om:hasUnit om:degreeCelsius ;
                sricats:hasBlockChainHash "0x3cd7e0ed2cddb2302ec872c818c938f37cbba882eba23fe28ab54f6cd2d77e2c" ;
                sricats:hasTrustabilityScore "0.8"^^xsd:float ;
                sosa:hasSimpleResult 2.2e+01 ;
                sosa:madeBySensor <http://www.w3.org/ns/sosa/Sensor/DHT11> ;
                sosa:observedProperty <http://www.w3.org/ns/sosa/observedProperty/STI_W201_temperature> ;
                sosa:resultTime "2022-12-02T21:00:01"^^xsd:dateTime .

            <http://www.w3.org/ns/sosa/Sensor/DHT11> a sosa:Sensor ;
                sosa:observes <http://www.w3.org/ns/sosa/Observation/DHT11_202212020001> .


        :return: string
        """
        shape_graph = """@prefix : <http://www.tekrajchhetri.com/sricats/> .
                            @prefix sosa: <http://www.w3.org/ns/sosa/> . 
                            @prefix sh: <http://www.w3.org/ns/shacl#> .
                            @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/>.
                            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

                          sosa:observationShape   a  sh:NodeShape ;
                           sh:targetClass sosa:Observation ;

                            sh:property
                            [
                                sh:path sosa:hasSimpleResult;
                                    sh:minCount 1;
                                    sh:maxCount 1;
                                    sh:minInclusive 0 ;
                                    sh:maxInclusive 100 ;
                                    sh:datatype  xsd:double;
                            ];

                            sh:property
                            [
                                sh:path :hasBlockChainHash; 
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:minLength 60 ; 
                                    sh:datatype  xsd:string;
                            ];

                            sh:property
                            [
                                sh:path sosa:resultTime; 
                                    sh:minCount 1;
                                    sh:maxCount 1;  
                                    sh:datatype xsd:dateTime;
                            ];
                            
                            sh:property
                            [
                                sh:path om:hasUnit; 
                                sh:minCount 1;
                                sh:maxCount 1;
                                sh:hasValue  om:degreeCelsius;
                            ];


                            sh:property
                            [
                                sh:path sosa:madeBySensor;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ];
                            sh:property
                            [
                                sh:path :hasTrustabilityScore; 
                                    sh:minCount 1;
                                    sh:maxCount 1;  
                                    sh:datatype  xsd:float;
                            ];
                            sh:property
                            [
                                sh:path sosa:observedProperty;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ]. 
                         sosa:observationSensorShape   a  sh:NodeShape ;
                           sh:targetClass sosa:Sensor ;
                            sh:property
                            [
                                sh:path sosa:observes;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ].


        """
        return shape_graph

    def relative_humidity(self):
        """ SHACL shape graph for relative humidity sensor

        Example Data Graph:
            <http://www.w3.org/ns/sosa/Observation/DHT11_202212020001> a sosa:Observation ;
                om:hasUnit om:percent ;
                sricats:hasBlockChainHash "0x3cd7e0ed2cddb2302ec872c818c938f37cbba882eba23fe28ab54f6cd2d77e2c" ;
                sricats:hasTrustabilityScore "0.8"^^xsd:float ;
                sosa:hasSimpleResult 2.2e+01 ;
                sosa:madeBySensor <http://www.w3.org/ns/sosa/Sensor/DHT11> ;
                sosa:observedProperty <http://www.w3.org/ns/sosa/observedProperty/STI_W201_temperature> ;
                sosa:resultTime "2022-12-02T21:00:01"^^xsd:dateTime .

            <http://www.w3.org/ns/sosa/Sensor/DHT11> a sosa:Sensor ;
                sosa:observes <http://www.w3.org/ns/sosa/Observation/DHT11_202212020001> .


        :return: string
        """
        shape_graph = """@prefix : <http://www.tekrajchhetri.com/sricats/> .
                            @prefix sosa: <http://www.w3.org/ns/sosa/> . 
                            @prefix sh: <http://www.w3.org/ns/shacl#> .
                            @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/>.
                            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

                          sosa:observationShape   a  sh:NodeShape ;
                           sh:targetClass sosa:Observation ;

                            sh:property
                            [
                                sh:path sosa:hasSimpleResult;
                                    sh:minCount 1;
                                    sh:maxCount 1;
                                    sh:minInclusive 0 ;
                                    sh:maxInclusive 100 ;
                                    sh:datatype  xsd:double;
                            ];

                            sh:property
                            [
                                sh:path :hasBlockChainHash; 
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:minLength 60 ; 
                                    sh:datatype  xsd:string;
                            ];
                            sh:property
                            [
                                sh:path :hasTrustabilityScore; 
                                    sh:minCount 1;
                                    sh:maxCount 1;  
                                    sh:datatype  xsd:float;
                            ];
                            
                            sh:property
                            [
                                sh:path sosa:resultTime; 
                                    sh:minCount 1;
                                    sh:maxCount 1;  
                                    sh:datatype xsd:dateTime;
                            ];
                            
                            sh:property
                            [
                                sh:path om:hasUnit;
                                sh:minCount 1;
                                sh:maxCount 1; 
                                sh:hasValue  om:percent;
                            ];


                            sh:property
                            [
                                sh:path sosa:madeBySensor;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ];

                            sh:property
                            [
                                sh:path sosa:observedProperty;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ]. 
                         sosa:observationSensorShape   a  sh:NodeShape ;
                           sh:targetClass sosa:Sensor ;
                            sh:property
                            [
                                sh:path sosa:observes;
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:nodeKind  sh:IRI;
                            ].


        """
        return shape_graph