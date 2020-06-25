print('Starting pyarrow test...', end='\n'*2)

import pyarrow.parquet as pq
import pyarrow as pa


table = pa.Table.from_arrays([list(range(0,10)), list(range(10,20))], names=['a', 'b'])

pq.write_table(table, 'foo.snappy.parquet', compression='snappy')

print(
    'ok, got up to here so far.' 
    'Created the Snappy encoded Parquet file, will try to read it now...'
    'Python might just crash suddenly.'
)

tbl = pq.read_table('foo.snappy.parquet')

print("good we got this far, means pyarrow worked correctly")
