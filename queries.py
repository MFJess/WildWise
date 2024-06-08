#############################
########## ANIMAIS ##########
#############################

# Características base e taxonómicas de um animal de id especificado
animal_characteristics = f'''PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>
SELECT ?id ?nome ?comprimento ?altura ?gestacao ?incubacao ?tempoVida ?dieta ?presas ?predadores ?nrEspecies ?tipoPele ?nomeCientifico ?reino ?familia ?ordem ?phylum ?classe ?genus
WHERE {{
  ?animal ont:idAnimal {id}.
    OPTIONAL {{ ?animal ont:idAnimal ?id. }}
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

# Localizações onde um animal de id especificado existe
animal_locations = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?localizacoes
WHERE {{
  ?animal ont:idAnimal {id}.
  ?animal ont:existeEm/ont:nomeLocalizacao ?localizacoes.
}}
'''

# Habitat onde um animal de id especificado habita
animal_habitats = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?habitats
WHERE {{
  ?animal ont:idAnimal {id}.
  ?animal ont:habitaEm/ont:nomeHabitat ?habitats.
}}
'''

# Colors of an animal de id especificado
animal_colors = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT ?cores
WHERE {{
  ?animal ont:idAnimal {id}.
  ?animal ont:coloracao/ont:nomeCor ?cores.
}}
'''

#############################
######### TAXONOMIA #########
#############################

# All kingdoms
all_kingdoms = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?reinos
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:reino ?reinos.
}}
'''

# All phylums
all_phylums = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?phylums
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:filo ?phylums.
}}
'''

# All classes
all_classes = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?classes
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:classe ?classes.
}}
'''

# All orders
all_orders = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?ordens
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:ordem ?ordens.
}}
'''

# All families
all_families = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?families
WHERE {{
  ?taxonomias a ont:Taxonomy.
  ?taxonomias ont:familia ?families.
}}
'''

# All genus 
all_genus = f'''
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
animal_by_kingdom = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:reino {kingdom};
  ont:nomeAnimal ?names.
}}
'''

# All animals that belong to a specified phylum
animal_by_phylums = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:filo {phylum};
  ont:nomeAnimal ?names.
}}
'''

# All animals that belong to a specified class
animal_by_classes = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:classe {classe};
  ont:nomeAnimal ?names.
}}
'''

# All animals that belong to a specified order
animal_by_orders = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:ordem {order};
  ont:nomeAnimal ?names.
}}
'''

# All animals that belong to a specified family
animal_by_families = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:familia {family};
  ont:nomeAnimal ?names.
}}
'''

# All animals that belong to a specified genus
animal_by_genus = f'''
PREFIX ont:<http://rpcw.di.uminho.pt/2024/4/untitled-ontology-34/>

SELECT DISTINCT ?names
WHERE {{
  ?animals ont:identificadoPor/ont:genus {genus};
  ont:nomeAnimal ?names.
}}
'''