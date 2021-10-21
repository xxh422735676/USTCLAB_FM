Theorem ex4: forall  P Q:Prop,
  (P/\Q)->(Q/\P).
Proof.
intros.
inversion H.
split.
apply H1.
apply H0.
Qed.