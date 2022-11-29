import { IDataTable, IDataTable2 } from './IDataTable';

export interface IHeaderTable<T = void> {
	text: string;
	value: keyof IDataTable;
	align?: 'start' | 'center' | 'end';
	sortable?: boolean;
	filterable?: boolean;
	groupable?: boolean;
	divider?: boolean;
	class?: string | string[];
	cellClass?: string | string[];
	width?: string | number;
	filter?: (value: any, search: string, item: T) => boolean;
	sort?: (a: any, b: any) => number;
	search?: (value: any, search: string, item: T) => boolean;
}

export interface IHeaderTable2<T = void> {
	text: string;
	value: keyof IDataTable2;
	align?: 'start' | 'center' | 'end';
	sortable?: boolean;
	filterable?: boolean;
	groupable?: boolean;
	divider?: boolean;
	class?: string | string[];
	cellClass?: string | string[];
	width?: string | number;
	filter?: (value: any, search: string, item: T) => boolean;
	sort?: (a: any, b: any) => number;
	search?: (value: any, search: string, item: T) => boolean;
}


