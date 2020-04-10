
from IngestDrugSynonyms import IngestDrugSynonyms
from DrugSynonymDataToNeo4j import DrugSynonymDataToNeo4j

drugSynonym = IngestDrugSynonyms()
drugSynonym.auto_get_and_clean_data()
drugSynonym.create_drug_study_links()

neo4jBridge = DrugSynonymDataToNeo4j()
neo4jBridge.merge_drugs_synonyms_and_link_between(drugSynonym.drug_vocab)
neo4jBridge.merge_studies(drugSynonym.all_studies_df)

# TODO drug - study

neo4jBridge.merge_drug_to_study_rels(drugSynonym.appeared_in_edges)

# TODO url - study
neo4jBridge.merge_url()
neo4jBridge.merge_url_to_study_rels()

