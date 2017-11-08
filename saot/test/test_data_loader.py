from saot import data_loader

ds = data_loader.load_data("../../data/test.csv")

print ds.target
print ds.query
print ds.data

print "Cleaning.."
ds.clean()
print ds.target
print ds.query
print ds.data
