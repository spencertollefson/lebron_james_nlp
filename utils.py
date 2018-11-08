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
    df[col_name] = df[col_name].str.replace(r"(\()*https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)(\))*",' ', regex=True)

    # Remove non-standard characters
    df[col_name] = df[col_name].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ", regex=True)
    df[col_name] = df[col_name].str.replace(r"@", "at", regex=True)

    # Strip whitespace
    df[col_name] = df[col_name].str.strip()

    # lowercase
    df[col_name] = df[col_name].str.lower()

    # Remove extra spaces
    df[col_name].replace(r"\s+",' ', regex=True, inplace=True)
    
    return df