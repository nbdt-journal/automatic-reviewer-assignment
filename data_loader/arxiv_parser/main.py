import pandas as pd 
import xml.etree.ElementTree as et 
def parse_XML(xml_file, df_cols): 
    """Parse the input XML file and store the result in a pandas 
    DataFrame with the given columns. 
    
    The first element of df_cols is supposed to be the identifier 
    variable, which is an attribute of each node element in the 
    XML data; other features will be parsed from the text content 
    of each sub-element. 
    """
    
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    rows = []
    
    for node in xroot: 
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        rows.append({df_cols[i]: res[i] 
                     for i, _ in enumerate(df_cols)})
    
    out_df = pd.DataFrame(rows, columns=df_cols)
        
    return out_df
xtree = et.parse("clean.xml")
xroot = xtree.getroot() 
df_cols = ["PMID", "ArticleTitle", "PubMedPubDate", "ArticleId"]
rows = []
s_ArticleTitle = ""
s_PubMedPubDate = ""
s_ArticleId = ""
s_PMID = ""
for node in xroot: 
    # s_PMID = node.attrib.get("PMID")
    # s_ArticleTitle = node.find("ArticleTitle").text  if node is not None else None
    s_PubMedPubDate = node.find("PubMedPubDate")
    s_PubMedPubDate = s_PubMedPubDate.text if s_PubMedPubDate is not None else ""
    # s_ArticleId = node.find("ArticleId").text  if node is not None else None
    
    rows.append({"PMID": s_PMID, "ArticleTitle": s_ArticleTitle, 
                 "PubMedPubDate": s_PubMedPubDate, "ArticleId": s_ArticleId})
out_df = pd.DataFrame(rows, columns = df_cols)
print(out_df)
df = pd.DataFrame(out_df)
df.to_csv('output_xml_to_csv.csv', index=False)