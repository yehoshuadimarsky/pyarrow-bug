print('Starting pyarrow test...', end='\n'*2)

import pyarrow.parquet as pq
import pyarrow as pa


table = pa.Table.from_arrays([list(range(0,10)), list(range(10,20))], names=['a', 'b'])

pq.write_table(table, 'foo.snappy.parquet', compression='snappy')

tbl = pq.read_table('foo.snappy.parquet')

assert False, "good we got this far, means pyarrow worked correctly"  # to raise an error
