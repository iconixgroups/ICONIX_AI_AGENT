```python
from flask import Blueprint, render_template, request
from src.template_library import Template

template_library_bp = Blueprint('template_library_bp', __name__)

@template_library_bp.route('/template_library', methods=['GET', 'POST'])
def template_library():
    if request.method == 'POST':
        selected_template = request.form.get('templateSelect')
        return redirect(url_for('src.ui.agent_builder.agent_builder', template=selected_template))
    else:
        templates = Template.query.all()
        return render_template('template_library.html', templates=templates)

@template_library_bp.route('/template/<template_id>', methods=['GET'])
def template_detail(template_id):
    template = Template.query.get_or_404(template_id)
    return render_template('template_detail.html', template=template)
```