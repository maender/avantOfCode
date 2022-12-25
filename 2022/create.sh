NUM=$1

echo "if __name__ == '__main__':\n\twith open('resources/day{$NUM}_small', 'r') as f:\n\t\tfor line in f.readlines():\n\t\t\tprint(line)\n" >> python/day$NUM.py
touch resources/day$NUM