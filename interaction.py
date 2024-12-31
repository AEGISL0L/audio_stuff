class ClassroomInteraction:
    def __init__(self):
        self.interaction_patterns = {
            'teacher_control': [],
            'student_responses': [],
            'retrospective_elicitations': []
        }
    
    def analyze_sequence(self, transcript: str):
        lines = transcript.split('\n')
        current_sequence = []
        
        for line in lines:
            # Track teacher control patterns
            if line.startswith('M:'):
                if '?' in line:
                    self.interaction_patterns['teacher_control'].append({
                        'type': 'question',
                        'content': line
                    })
                    
            # Track student responses
            elif any(student in line for student in ['Sharon:', 'Karen:']):
                self.interaction_patterns['student_responses'].append({
                    'student': line.split(':')[0],
                    'response': line.split(':')[1]
                })
                
            # Identify retrospective elicitations
            if len(current_sequence) > 0 and line.startswith('M:'):
                if any(prev['response'] in line for prev in self.interaction_patterns['student_responses'][-3:]):
                    self.interaction_patterns['retrospective_elicitations'].append({
                        'original': current_sequence[-1],
                        'elicitation': line
                    })
            
            current_sequence.append(line)
            
        return self.interaction_patterns