import csv

from parse import parse


def main():
	file_path = 'D:\chromeDownload\云3 只读库慢日志明细.csv'
	with open(file_path, 'r', encoding='utf-8') as csv_file:
		read = csv.DictReader(csv_file)
		filter_list = list(filter(lambda row: 'opserver_callback_params' in row['SQL'], read))
		tenant_id_info = {}
		for e in filter_list:
			if '7653' in e['SQL']:
				print(e)
			r = parse("SELECT {select} FROM opserver_callback_params WHERE ({where} tenant_id = '{tenant_id}')", e['SQL'])
			tenant_id_info.setdefault(r['tenant_id'], {'count': 0, '执行耗时（秒）': 0})
			info = tenant_id_info[r['tenant_id']]
			info['count'] += 1
			info['执行耗时（秒）'] += float(e['执行耗时（秒）'])

	print(tenant_id_info)
	for tenant_id in tenant_id_info:
		info = tenant_id_info[tenant_id]
		print(tenant_id, info, info['执行耗时（秒）'] / info['count'])
	pass


if __name__ == '__main__':
	main()
