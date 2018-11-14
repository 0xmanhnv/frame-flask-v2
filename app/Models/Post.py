from app import db, ma

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	thumbnail = db.Column(db.String(255), nullable=True)
	description = db.Column(db.Text(), nullable=True)
	created_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now())
	updated_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now(), server_onupdate=db.func.now())

	"""
	"Chuyển các thuộc tính về thành chuỗi
	"""
	def __repr__(self):
		return str(self.__dict__)

"""
"Tạo Schema cho model
"""
class PostSchema(ma.ModelSchema):
	class Meta:
		fields = ('id','title', 'thumbnail')
