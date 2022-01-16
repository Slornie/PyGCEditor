from PyQt5.QtWidgets import QHeaderView, QTableWidget

class QtTableWidgetFactory():
    '''Factory for table widgets'''
    def __init__(self):
        pass
    
    def construct(self, label = ["Empty"], columns = 1, stretch = True) -> QTableWidget:
        '''Constructs an arbitrary table widget'''
        tableWidget: QTableWidget = QTableWidget()
        tableWidget.setColumnCount(columns)
        tableWidget.setHorizontalHeaderLabels(label)
        
        if stretch:
            tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        else:
            tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
            tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setSortingEnabled(True)
        return tableWidget

    