'''
Utils.py
Spencer Tollefson
November 7, 2018
For use with lebronjames_sentiment_analysis project
'''

def string_clean_df_column(df, col_name):
    '''
    df: DataFrame which contains the column
    col_name: Name of column in DF one wants to perform cleaning operations to
    returns: entire DataFrame, with cleaned column
    '''
   
    # remove URLs and parantheses surrounding URLs
    df[col_name] = df[col_name].str.replace(r"(\()*https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)(\))*"," ", regex=True)
    
    # Chance strange character to contraction symbol
    df[col_name] = df[col_name].str.replace(r"’", "'", regex=True)

    # Remove non-standard characters and numbers
    df[col_name] = df[col_name].str.replace(r"[^A-Za-z(),!?@\'\`\"\_\n]", " ", regex=True)
    df[col_name] = df[col_name].str.replace(r"@", "at", regex=True)

    # Drop other non-alphas
    df[col_name] = df[col_name].str.replace(r"[(),!?\`\"\_]", " ", regex=True)
    
    # Strip whitespace
    df[col_name] = df[col_name].str.strip()

    # lowercase
    df[col_name] = df[col_name].str.lower()

    # Remove extra spaces
    df[col_name].replace(r"\s+"," ", regex=True, inplace=True)
    
    # Drop any cell with only "full quote" as the body
    df = df.loc[df.body != 'full quote', :]

    return df