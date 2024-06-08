#############################
########## ANIMAIS ##########
#############################

# Todos os animais
def all_animals(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?idAnimal ?nome
WHERE {{
  ?a a ont:Animal.
  ?a ont:idAnimal ?idAnimal .
  ?a ont:nomeAnimal ?nome.
}}
'''

# Características base e taxonómicas de um animal de id especificado
def animal_characteristics(id): return f'''PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>
SELECT ?idAnimal ?nome ?comprimento ?altura ?gestacao ?incubacao ?tempoVida ?dieta ?presas ?predadores ?nrEspecies ?tipoPele ?nomeCientifico ?reino ?familia ?ordem ?phylum ?classe ?genus
WHERE {{
  ?animal ont:idAnimal {id}.
    OPTIONAL {{ ?animal ont:idAnimal ?idAnimal. }}
    OPTIONAL {{ ?animal ont:nomeAnimal ?nome. }}
    OPTIONAL {{ ?animal ont:comprimento ?comprimento. }}
    OPTIONAL {{ ?animal ont:altura ?altura. }}
    OPTIONAL {{ ?animal ont:incubacao ?incubacao. }}
    OPTIONAL {{ ?animal ont:tempoVida ?tempoVida. }}
    OPTIONAL {{ ?animal ont:dieta ?dieta. }}
    OPTIONAL {{ ?animal ont:presas ?presas. }}
    OPTIONAL {{ ?animal ont:predadores ?predadores. }}
    OPTIONAL {{ ?animal ont:nrEspecies ?nrEspecies. }}
    OPTIONAL {{ ?animal ont:tipoPele ?tipoPele. }}
    
    ?animal ont:identificadoPor ?taxonomia.
    OPTIONAL {{ ?taxonomia ont:nomeCientifico ?nomeCientifico. }}
    OPTIONAL {{ ?taxonomia ont:reino ?reino. }}
    OPTIONAL {{ ?taxonomia ont:familia ?familia. }}
    OPTIONAL {{ ?taxonomia ont:ordem ?ordem. }}
    OPTIONAL {{ ?taxonomia ont:classe ?classe. }}
    OPTIONAL {{ ?taxonomia ont:genus ?genus. }}
    OPTIONAL {{ ?taxonomia ont:phylum ?phylum. }}    
}} '''

# Animais por localizaçao
def animal_locations(local): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?idAnimal ?nome
WHERE {{
  ?a a ont:Animal.
  ?animal ont:existeEm/ont:nomeLocalizacao {local}.
  ?a ont:idAnimal ?idAnimal .
  ?a ont:nomeAnimal ?nome.
}}
'''

# Animais que habitam
def animal_habitats(habitat): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?idAnimal ?nome
WHERE {{
  ?a a ont:Animal.
  ?a ont:habitaEm/ont:nomeHabitat {habitat}.
  ?a ont:idAnimal ?idAnimal .
  ?a ont:nomeAnimal ?nome.
}}
'''

# Animais com certa cor
def animal_colors(color): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?idAnimal ?nome
WHERE {{
  ?a a ont:Animal.
  ?a ont:coloracao/ont:nomeCor {color}.
  ?a ont:idAnimal ?idAnimal .
  ?a ont:nomeAnimal ?nome.
}}
'''

#############################
######### TAXONOMIA #########
#############################

# All kingdoms
def all_kingdoms(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?reinos
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:reino ?reinos.
}}
'''

# All phylums
def all_phylums(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?phylums
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:filo ?phylums.
}}
'''

# All classes
def all_classes(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?classes
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:classe ?classes.
}}
'''

# All orders
def all_orders(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?ordens
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:ordem ?ordens.
}}
'''

# All families
def all_families(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?families
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:familia ?families.
}}
'''

# All genus 
def all_genus(): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?genus
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:genero ?genus.
}}
'''


######################################
######### ANIMAIS-TAXONOMIAS #########
######################################

# All animals that belong to a specified kingdom
def animal_by_kingdom(kingdom): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:reino {kingdom};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''

# All animals that belong to a specified phylum
def animal_by_phylums(phylum): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:filo {phylum};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''

# All animals that belong to a specified class
def animal_by_classes(classe): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:classe {classe};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''

# All animals that belong to a specified order
def animal_by_orders(order): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:ordem {order};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''

# All animals that belong to a specified family
def animal_by_families(family): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:familia {family};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''

# All animals that belong to a specified genus
def animal_by_genus(genus): return f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?idAnimal ?nome
WHERE {{
  ?animals ont:identificadoPor/ont:genus {genus};
  ont:idAnimal ?idAnimal;
  ont:nomeAnimal ?nome.
}}
'''