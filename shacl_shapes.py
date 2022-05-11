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
            @prefix : <http://www.tekrajchhetri.com/sricats/> .
            @prefix sosa: <http://www.w3.org/ns/sosa/> .
            @prefix sh: <http://www.w3.org/ns/shacl#> .
            @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

            <observation/DS18B20_202205114824259234> a sosa:Observation ;
                om:hasUnit om:degreeCelsius ;
                sricats:hasHash "21449ca6d0e585d666dac4c24f51c1a0c047e2d45f229fddbaf115361d843c24"^^xsd:string ;
                sosa:hasSimpleResult 8.1e+01 ;
                sosa:madeBySensor <sensor/DS18B20> ;
                sosa:observedProperty <STI_W201_temperature> ;
                sosa:resultTime "2022-05-11T09:48:24"^^xsd:dateTime .

            <sensor/DS18B20> a sosa:Sensor ;
                sosa:observes <observation/DS18B20_202205114824259234> .

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
                                sh:path :hasHash; 
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:minLength 64 ;
                                    sh:maxLength 64 ;
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
            @prefix : <http://www.tekrajchhetri.com/sricats/> .
            @prefix sosa: <http://www.w3.org/ns/sosa/> .
            @prefix sh: <http://www.w3.org/ns/shacl#> .
            @prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

            <observation/DS18B20_2022051010211961971> a sosa:Observation ;
                    :hasHash "c38f83392718b1024aff70b5fd0d79fdc04ee55fba7458554e6326f8b08bdf42" ;
                    om:hasUnit om:percent;
                    sosa:resultTime "2005-02-28T00:00:00"^^xsd:dateTime;
                    sosa:hasSimpleResult "45.3"^^xsd:double ;
                    sosa:madeBySensor <sensor/DS18B20> ;
                    sosa:observedProperty <STI_W201_humidity> .

            <sensor/DS18B20> a sosa:Sensor ;
                sosa:observes <observation/DS18B20_2022051010211961971> .

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
                                sh:path :hasHash; 
                                    sh:minCount 1;
                                    sh:maxCount 1; 
                                    sh:minLength 64 ;
                                    sh:maxLength 64 ;
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