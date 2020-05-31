import glob, os

def get_brand(file):
    dir = os.path.dirname(file)  ## dir of dir of file
    return os.path.split(dir)[1]

def dump(file = "data/brands.txt"):
    brands = list(labels)
    brands.sort()
    with open(file, 'w') as f:
        for item in brands:
            f.write("%s\n" % item)

dataset = []
labels = set()

for file in glob.glob("data/labels/**/*.jpeg"):
    brand = get_brand(file)
    dataset.append([file, brand])
    labels.add(brand)

# Use to update brands file
#dump()

