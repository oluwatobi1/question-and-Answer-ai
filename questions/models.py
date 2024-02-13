from django.db import models


class PDFDocument(models.Model):
    title = models.CharField(blank=True, max_length=255)
    pdf_file = models.FileField(upload_to='pdf_files/')
    pdf_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pdf_file.name
