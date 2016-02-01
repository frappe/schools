# Student Applicant

A Student Applicant record needs to be created when a student applies for a programe at the institute.
You can Approve or Reject a student applicant. By accepting a student applicaant you add them to the students list.

<img class="screenshot" alt="Student Applicant" src="{{url_prefix}}/assets/img/student/student-applicant.png">

### Application Status

- By default when a student applicant is created in the system, the application status is set to 'Applied'

- You can update the status to 'Approved' once you approve the applicant to join your institute.

- Once the application status is set to 'Approved', the 'Enroll' button should show up. 
	You can create a student record against the student applicant by clicking on this button.
	
- Once a student is created against the student applicant, the system shall set the application status to 'Admitted' 
	and will not allow you to change the application status unless the student record is deleted.

### Student Enrollment


Once you approve a Student Applicant you can enroll them to a program. Select the 'Enroll' buttom,
the system shall create a student against that applicant and redirect you to the [Program Enrollment form]({{docs_base_url}}/user/guides/student/program-enrollment.html).

<img class="screenshot" alt="Student Applicant Enrollment" src="{{url_prefix}}/assets/img/student/student-applicant-enroll.png">

{next}