#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:51:22 2021

@author: chiew256
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "/Users/chiew256/data-science-salary/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)