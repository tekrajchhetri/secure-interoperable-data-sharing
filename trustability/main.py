# -*- coding: utf-8 -*-
# @Time    : 02.12.22 17:28
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : main.py
# @Software: PyCharm

from typing import Union
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    # taken from getbootstrap.com
    index="""

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Tek Raj Chhetri">  

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <!-- Favicons -->


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      .b-example-divider {
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }

      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }

      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }
    </style>

  </head>
  <body>
    
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <symbol id="check" viewBox="0 0 16 16">
    <title>Check</title>
    <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
  </symbol>
</svg>

<div class="container py-3">
  <header>
    <div class="d-flex flex-column flex-md-row align-items-center pb-3 mb-4 border-bottom">



    <div class="pricing-header p-3 pb-md-4 mx-auto text-center">
      <h1 class="display-4 fw-normal">Trustability</h1>
      <p class="fs-5 text-muted">
      Below are the defined parameters and their corresponding trustability score. Details are available in the paper.<br>
      For API document visit base_url/docs. Example: http://localhost:8000/docs.
      </p>
    </div>
  </header>


    <h2 class="display-6 text-center mb-4">Example Sources</h2>

    <div class="table-responsive">
      <table class="table text-center">
        <thead>
          <tr>
            <th style="width: 14%;">SN</th>
            <th style="width: 22%;">Manufacturer</th>  
            <th style="width: 22%;">Location (City)</th> 
            <th style="width: 22%;">Deployed By</th>  
          </tr>
        </thead>
    

        <tbody>
          <tr> 
            <td>1</td> 
            <td>Bosch</td> 
            <td>Innbsruck</td> 
            <td>Bosch</td> 
          </tr>
          <tr>
            <td>2</td> 
            <td>Texas Instruments</td> 
            <td>Yishun</td> 
            <td>Bosch</td> 
          </tr>
          <tr>
            <td>3</td> 
            <td>-</td> 
            <td>Innbsruck</td> 
            <td>STI</td> 
          </tr>
          <tr>
            <td>4</td> 
            <td>-</td> 
            <td>Innbsruck</td> 
            <td>-</td> 
          </tr>
        </tbody>
      </table>
    </div>
  </main>
<center>&copy; Tek Raj Chhetri; Web: <a href="https://tekrajchhetri.com/" target="_blank">https://tekrajchhetri.com/</a>
</center>
 
    </div>
  </footer>
</div>


    
  </body>
</html>

    """
    return index


class Trustability(BaseModel):
    sensor_manufacturers: str
    deployed_location: str
    deployed_by: str

class Response(BaseModel):
    trustability: float


@app.post("/trustability/", response_model=Response)
def trustability(trustability_items: Trustability):
    sensor_manufacturers = ["bosch","honeywell", "texas instruments"]
    deployed_location = ["innsbruck", "tartu", "Yishun"]
    deployed_by = ["sti", "texas instruments", "bosch"]
    weights = [0.5, 0.2,0.3]

    trustability_score=0.0
    trustfactors = [trustability_items.sensor_manufacturers.lower() in sensor_manufacturers,
     trustability_items.deployed_location.lower() in deployed_location,
     trustability_items.deployed_by.lower() in deployed_by]
    trustfactorsInt = np.array(trustfactors).astype(int)
    trustability_score = trustfactorsInt[0]*weights[0]+trustfactorsInt[1] * weights[1]+trustfactorsInt[2] * weights[2]

    return {"trustability":trustability_score}
