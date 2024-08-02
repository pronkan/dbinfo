from functools import cache
from tabulate import tabulate
import logging


# Data structure class for single DB info
class DBInfo:
    """
    Class to store DB info and do necessary calculations
    """

    class TP:  # TP is for Table Parameter
        def __init__(self, value: any, name: str):
            self.value = value
            self.name = name
            if isinstance(value, float):
                self.value = round(value, 3)
            if value is None:
                self.value = "N/A"

    def __init__(
        self,
        name,
        application,
        storage_type,
        storage_size,
        storage_used,
        engine,
        private_endpoint,
        tags,
        status,
        **kwargs,
    ):
        self.name = self.TP(name, "DB name")
        self.application = self.TP(application, "Application name")
        self.status = self.TP(status, "DB status")
        self.storage_type = self.TP(storage_type, "Storage type")
        self.storage_size = self.TP(storage_size, "Storage size")
        self.storage_used = self.TP(storage_used, "Storage used")
        self.engine = self.TP(engine, "DB engine")
        self.private_endpoint = self.TP(private_endpoint, "Private endpoint")
        self.tags = tags
        self.other = kwargs

    # Added decorator to cache calculation result for future calls, saves time on multiple calls
    @property
    @cache
    def storage_used_pst(self) -> TP:
        """
        Calculate storage used percentage
        :return: float value of storage percentage usage
        """
        logging.debug(f"Calculating storage used percentage for {self.name.value}")
        logging.debug(f"Storage used: {self.storage_used.value}")
        logging.debug(f"Storage size: {self.storage_size.value}")
        if "N/A" in (self.storage_used.value, self.storage_size.value):
            return self.TP("N/A", "Storage used %")
        pst_used = self.storage_used.value / self.storage_size.value * 100
        return self.TP(pst_used, "Storage used %")

    def table_info(self) -> tuple:
        """
        Return main info about DB (according to the task)
        This function is used to form table output dynamically so we can add or remove any info about DB
        :return: tuple of DB info objects
        """
        return (
            self.name,
            self.storage_type,
            self.storage_size,
            self.storage_used,
            self.storage_used_pst,
        )


# def table_horizontal_delimiters(header_sections: list) -> str:
#     """
#     Create table horizontal delimiters according to the header sections for prettiness and readability
#     :param header_sections: list of header sections with '|' delimiters
#     :return: horizontal delimiter string
#     """
#     table = '|'
#     for section in header_sections:
#         if len(section) <= 2:
#             continue
#         table += '-' * len(section)
#         table += '|'
#     table += '\n'
#     return table


def sorted_tabel(databases: list) -> str:
    """
    Form a sorted table output in form of a readable table

    Here I started to form tabe the old fashion way, but when finished I remembered about tabulate.
    I left the old code commented out for reference.
    :param databases: list of sorted databases
    :return: multi-line string table
    """
    tab_table = [[item.name for item in databases[0].table_info()]]
    # Create table header
    # table_header = ''
    # for item in databases[0].table_info():
    #     table_header += f'| {item.name} '
    # table_header += '|\n'
    # delimiter = table_horizontal_delimiters(table_header.split('|'))
    # table = delimiter
    # table += table_header
    # table += delimiter
    # Add data to table
    for db in databases:
        tab_table.append([item.value for item in db.table_info()])
        # for i in db.table_info():
        #     table += f'| {i.value} '
        # table += '|\n'
        # table += delimiter
    # return table
    return tabulate(tab_table, headers="firstrow", tablefmt="grid")


def sort_list(databases: list) -> list:
    """
    Sort list of DBInfo objects by storage used percentage
    :param databases:
    :return:
    """
    return sorted(
        databases,
        key=lambda x: (
            x.storage_used_pst.value if x.storage_used_pst.value != "N/A" else 0
        ),
        reverse=True,
    )
