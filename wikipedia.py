import wikipedia
import os
import sys
print("""
░██╗░░░░░░░██╗██╗██╗░░██╗██╗██████╗░███████╗██████╗░██╗░█████╗░
░██║░░██╗░░██║██║██║░██╔╝██║██╔══██╗██╔════╝██╔══██╗██║██╔══██╗
░╚██╗████╗██╔╝██║█████═╝░██║██████╔╝█████╗░░██║░░██║██║███████║
░░████╔═████║░██║██╔═██╗░██║██╔═══╝░██╔══╝░░██║░░██║██║██╔══██║
░░╚██╔╝░╚██╔╝░██║██║░╚██╗██║██║░░░░░███████╗██████╔╝██║██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝
--Creado por Hector Diaz
--Herramienta para buscar mas rapido en wikipedia""")
language = "es"
wikipedia.set_lang(language)
#print(f"Resumen en {language}:", wikipedia.page(search1).summary)
search1 = input("Buscar: ")
print(wikipedia.summary(search1))
search2 = search1
print("Resultados de "+search1+": ",search1)
page = wikipedia.page(search1[0])
title = page.title
categories = page.categories
content = page.content
links = page.links
references = page.references
summary = page.summary
print("Contenido:\n", content, "\n")
print("Titulo:" ,title, "\n")
print("Categorias:", categories, "\n")
print("Links:", links, "\n")
print("Referencias:" ,references, "\n")
print("Resumen:", summary, "\n")
#Creado por Héctor Diaz
#Sigueme en mi github https://github.com/Kris011
