from typing import List
from pyspark.sql import DataFrame
from delta.tables import DeltaTable
from pyspark.sql.functions import current_timestamp
from pyspark.sql.window import Window
from pyspark.sql.functions import concat , col , row_number

class transformations:

    def dedup(self , df:DataFrame , dedup_cols:List , cdc:str):

        df = df.withColumn("dedupKey" , concat(*dedup_cols))
        df = df.withColumn("dedupCounts" , row_number().over(Window.partitionBy("dedupKey").orderBy(col(cdc).desc())))
        df = df.filter(col('dedupCounts') == 1)
        df = df.drop("dedupKey" , "dedupCounts")
                     
        return df
    
    def process_timestamp(self , df):
        
        df = df.withColumn("process_timestamp",current_timestamp())
        return df
    
    def upsert(self ,spark ,  df , key_cols , table , cdc):
        marge_condition = "AND".join([f"src.{i} = trg.{i}" for i in key_cols])
        dlt_obj = DeltaTable.forName(spark , f"pysparkdbt.silver.{table}")
        dlt_obj.alias("trg").merge(df.alias("src"),marge_condition)\
            .whenMatchedUpdateAll(condition = f"src.{cdc} >= trg.{cdc}")\
            .whenNotMatchedInsertAll()\
            .execute()
        return 1









