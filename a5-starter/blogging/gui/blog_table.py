import sys
from PyQt6.QtCore import Qt, QAbstractTableModel


from blogging.controller import Controller
from blogging.blog import Blog


class BlogTableView(QAbstractTableModel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.blogs = []
        # self.refresh_data()

    def refresh_data_search(self, search_string):
        self.blogs = []
        liblogs = self.controller.retrieve_blogs(search_string)

        for blog in liblogs:
            row = []
            row.append(blog.id)
            row.append(blog.name)
            row.append(blog.url)
            row.append(blog.email)

            self.blogs.append(row)
        # emit the layoutChanged signal to alert the QTableView of model changes
        self.layoutChanged.emit()
    def refresh_data(self):
        self.blogs = []
        liblogs = self.controller.list_blogs()
        for blog in liblogs:
            row = []
            row.append(blog.id)
            row.append(blog.name)
            row.append(blog.url)
            row.append(blog.email)

            self.blogs.append(row)
        # emit the layoutChanged signal to alert the QTableView of model changes
        self.layoutChanged.emit()

    def data(self, index, role):
        value = self.blogs[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            # Perform per-type checks and render accordingly.
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value
            if isinstance(value, str):
                # Render strings with quotes
                return '%s' % value
            # Default (anything not captured above: e.g. int)
            return value


        if role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight


    def rowCount(self, index):
        # The length of the outer list.
        return len(self.blogs)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if self.blogs:
            return len(self.blogs[0])
        else:
            return 0

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = ['ID', 'Name', 'URL', 'Email']
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return '%s' % headers[section]
        return super().headerData(section, orientation, role)
