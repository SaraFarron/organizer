from sqlalchemy import DECIMAL, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class ChartData(Base):
    __tablename__ = "chartdata"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    y_axis_name = Column(String)
    x_axis_name = Column(String)


class ChartPoint(Base):
    __tablename__ = "chartpoint"
    id = Column(Integer, primary_key=True, index=True)
    y_value = Column(DECIMAL(10, 2))
    x_value = Column(Date)
    chart_data_id = Column(Integer, ForeignKey("chartdata.id"))
    chart_data = relationship("ChartData", back_populates="points")
