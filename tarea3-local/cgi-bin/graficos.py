#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import sys
import cgi
import json

import grafico_barra
import grafico_linea
import grafico_torta

graficos = grafico_barra.gbarra+grafico_torta.gtorta+grafico_linea.glinea


print(json.dumps(graficos))
#print(json.dumps("hola"))