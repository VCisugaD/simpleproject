from PyQt5.QtCore import QAbstractTableModel, Qt


class PdTable(QAbstractTableModel):
    def __init__(self, data, showAllColumn=False):
        QAbstractTableModel.__init__(self)
        self.showAllColumn = showAllColumn
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if type(self._data.columns[col]) == tuple:
                return self._data.columns[col][-1]
            else:
                return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return (self._data.axes[0][col])
        return None