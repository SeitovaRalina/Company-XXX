import collections
number = "%02d" % (11,)
f = open(f'input_s1_{number}.txt')

def update_name(str):
    if len(str.split()) > 1:
        names[str[:4]] = str[5:]
    else:
        if str[:4] not in names:
            names[str[:4]] = 'Unknown Name'

names = {}
dependencies = collections.defaultdict(list)
while True:
    boss = f.readline().rstrip()
    boss_id = boss[:4]
    worker = f.readline().rstrip()
    worker_id = worker[:4]
    if boss_id != 'END':
        update_name(boss)
        update_name(worker)
    else:
        break
    dependencies[boss_id].append(worker_id)
    for bos in dependencies:
        if bos != boss_id and boss_id in dependencies[bos]:
                dependencies[bos].append(worker_id)
    if worker_id in dependencies:
        dependencies[boss_id] += dependencies[worker_id]

id = worker_id
if len(worker) != 4:
    id = ''
    for key, value in names.items():
        if value == worker:
            id = key
            break
if id in dependencies:
    for wrk in sorted(dependencies[id]):
        print(wrk, names[wrk])
else: print('NO')
print('-'*30)
with open(f'output_s1_{number}.txt') as file:
    for line in file:
        print(line.rstrip())