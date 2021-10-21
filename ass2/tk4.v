Theorem ex4: forall P Q R:Prop,
  (P/\(Q/\R))->((P/\Q)/\R).
Proof.
intros.
split.
split.
inversion H.
inversion H1.
apply H0.
inversion H.
inversion H1.
apply H2.
inversion H.
inversion H1.
apply H3.
Qed.