import os

os.system('mkdir OBs')
targets = open('props.txt','r').readlines()

for target in targets:
	lines = open('ref.obx','r').readlines()

	name = target.split()[0]
	ra = target.split()[1]
	dec = target.split()[2]
	vmag = target.split()[3]
	texp = target.split()[4]
	
	tline = lines[8]
	tline = tline.replace('refname',name)
	lines[8] = tline

	tline = lines[13]
	tline = tline.replace('refra',ra)
	lines[13] = tline

	tline = lines[14]
	tline = tline.replace('refdec',dec)
	lines[14] = tline

	tline = lines[24]
	tline = tline.replace('refname',name)
	lines[24] = tline

	tline = lines[32]
	tline = tline.replace('refmag',vmag)
	lines[32] = tline

	tline = lines[57]
	tline = tline.replace('reftexp',texp)
	lines[57] = tline

	f = open('OBs/'+name+'.obx','w') 
	f.writelines(lines)
	f.close()


	