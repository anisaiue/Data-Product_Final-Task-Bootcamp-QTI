FROM python:3.7

#Mengatur working directory sebagai app
WORKDIR /app 
 
#Installing python packages
RUN pip install pandas scikit-learn flask
 
# Copy semua file
COPY . .
 
#Expose port 5000 dari container
EXPOSE 5000

#Starting the python application
CMD ["python", "app.py"]
